def transform(data):
    transformed_data = []

    for keyword, content in data.items():
        if "data" in content:
            for item in content["data"]:
                location_id = item.get("location_id", "-")
                location_name = item.get("name", "-")

                address = item.get("address_obj", {})
                province = address.get("city", "-")

                transformed_data.append([
                    location_id,
                    location_name,
                    province,
                    keyword
                ])

    return transformed_data

#transformed_data = transform(run_queries())
#print(transformed_data)