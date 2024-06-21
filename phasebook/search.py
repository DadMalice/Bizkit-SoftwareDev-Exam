from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!

    id = args.get('id')
    name = args.get('name')
    age = args.get('age')
    occupation = args.get('occupation')

    results = []

    #Results based on ID
    if id:
        user = next((user for user in USERS if user['id'] == id), None)
        if user and user not in results:
            results.append(user)

    #Results based on Name
    if name:
        for user in USERS:
            if name.lower() in user['name'].lower() and user not in results:
                results.append(user)

    #Results based on Age
    if age:
        try:
            age = int(age)
            for user in USERS:
                if age - 1 <= user['age'] <= age + 1 and user not in results:
                    results.append(user)
        except ValueError:
            pass

    #Results based on Occupation
    if occupation:
        for user in USERS:
            if occupation.lower() in user['occupation'].lower() and user not in results:
                results.append(user)

    #If no parameters are provided, return all users
    if not any([id, name, age, occupation]):
        return USERS
    
    return results
