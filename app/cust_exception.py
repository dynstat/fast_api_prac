from fastapi.responses import JSONResponse


# imp: must not be a async func
def validation_exception_handler(request, exc):
    """Handles Exception during validations in request parameters and values.

    Args:
        request (request): http object
        exc (Exception): Exception

    Returns:
        JSONResponse: returns the JSONResponse instance
    """
    exc_list = exc.errors()
    resp_json_list = []
    for e in exc_list:
        temp_dict = {}
        std_err_mssg = e["msg"]
        type_ = e["loc"][0]
        name = e["loc"][1]
        add_info = f"422 ERROR - Please check the type of {type_} named {name}."  # creating a custom field.
        # filling the temp dictionary
        temp_dict[type_] = name
        temp_dict["std error"] = std_err_mssg
        temp_dict["additional info"] = add_info

        # appending this temp dict to resp_json_list
        resp_json_list.append(temp_dict)

    path_params = request.path_params
    query_params = request.query_params._dict
    # return PlainTextResponse(str(exc), status_code=422)
    return JSONResponse(
        resp_json_list,
        status_code=422,
    )
