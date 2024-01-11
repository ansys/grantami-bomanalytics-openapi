import importlib
from .examples import example_dict

models_module = importlib.import_module("ansys.grantami.bomanalytics_openapi.models")


def get_example(model_definition):
    try:
        return example_dict[model_definition.__name__]
    except KeyError:
        return


def generate_model(model_definition):
    example = get_example(model_definition)
    arg_dict = get_arg_dict(example, model_definition)
    return model_definition(**arg_dict)


def get_arg_dict(values, model_class):
    all_types = values.keys()
    complex_types = model_class.subtype_mapping.keys()
    simple_types = [t for t in all_types if t not in complex_types]

    simple_ctor_arguments = {
        get_python_arg_name(model_class, arg): values[arg] for arg in simple_types
    }
    complex_ctor_arguments = {
        get_python_arg_name(model_class, arg): get_complex_arg_value(
            values, arg, model_class
        )
        for arg in complex_types
    }

    return {**simple_ctor_arguments, **complex_ctor_arguments}


def get_complex_arg_value(values, arg, model_class):
    arg_value = values[arg]
    class_name = model_class.subtype_mapping[arg]
    sub_class = getattr(models_module, class_name)
    if arg_value:
        results = []
        if isinstance(arg_value, dict):
            # Dictionary of primitives
            args = {}
            for rest_name, value in arg_value.items():
                python_arg_name = get_python_arg_name(sub_class, rest_name)
                args[python_arg_name] = value
            obj = sub_class(**args)
            results.append(obj)
        elif isinstance(arg_value, str):
            # Enum: value is str
            results.append(arg_value)
        else:
            # List of complex types
            for example_value in arg_value:
                args = get_arg_dict(example_value, sub_class)
                obj = sub_class(**args)
                results.append(obj)
        return results


def get_python_arg_name(model_class, arg):
    for python_arg, api_arg in model_class.attribute_map.items():
        if api_arg == arg:
            return python_arg


def mock_method(mocker, verb, url, response_json):
    mocker_method = getattr(mocker, verb.lower())
    mocker_method(url, json=response_json)
