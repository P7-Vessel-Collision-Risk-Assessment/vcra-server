from fastapi import HTTPException

def slice_query_validation(latitude_range: str, longitude_range: str):
    
    try:
        latitude_range = latitude_range.split(",")
        longitude_range = longitude_range.split(",")
    except:
        raise HTTPException(status_code=400, detail=f"Expected query parameters latitude_range and longitude_range, got {latitude_range}, {longitude_range}")

    if len(latitude_range) != 2:
        raise HTTPException(status_code=400, detail=f"Latitude range expected 2 arguments (min,max) got: {latitude_range}")

    if len(longitude_range) != 2:
        raise HTTPException(status_code=400, detail=f"Longitude range expected 2 arguments (min,max) got: {longitude_range}")

    try:
        lat_min = float(latitude_range[0])
        lat_max = float(latitude_range[1])
        long_min = float(longitude_range[0])
        long_max = float(longitude_range[1])
    except:
        raise HTTPException(status_code=400, detail="Latitude and Longitude must be numbers")
    
    if lat_min > lat_max:
        raise HTTPException(status_code=400, detail=f"Expected first argument to be smaller than second argument, got: latitude_min: {lat_min}, latitude_max: {lat_max}")

    if long_min > long_max:
        raise HTTPException(status_code=400, detail=f"Expected first argument to be smaller than second argument, got: longitude_min: {long_min}, longitude_max: {long_max}")
    
    return (lat_min, lat_max), (long_min, long_max)