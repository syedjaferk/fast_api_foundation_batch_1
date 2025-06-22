

#business logic
def item_value(item_id, name):
    return {"item_id": item_id, "name": name}

if __name__ =="__main__":
    print(item_value(123, "jafer"))