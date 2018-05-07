import requests
# TODO: refactor to OOP

url = 'http://pulse-rest-testing.herokuapp.com/'
url_roles = url + 'roles/'


def create_obj(url, data):
    request = requests.post(url, data=data)
    return request.json()['id']


def get_by_id(url, id):
    request = requests.get(url + str(id))
    assert request.status_code == 200
    response = request.json()

    obj = {'id': response['id'],
           'name': response['name'],
           'type': response['type'],
           'level': response['level'],
           'book': response['book']}
    try:
        assert id == obj.get('id')
        return obj
    except Exception:
        return 'Error occurred during your request!'

def get_in_list(url, obj):
    response = requests.get(url)
    try:
        assert obj in response.json()
        return 'Success. Object exists in list!'
    except Exception:
        return 'Error occurred during your request!'


def edit_obj(url, id, updated_data):
    request = requests.put(url + str(id), data=updated_data)
    return request.status_code


def assure_updated(url, upd_obj, id):
    obj = get_by_id(url, id)
    obj.pop('id')
    try:
        assert obj == upd_obj
        return 'Success!'
    except AssertionError:
        return 'Failed!'


def delete_obj(url, id):
    response = requests.delete(url + f'{id}')
    return response.status_code


if __name__ == '__main__':
    role = {"name": "Hagrid",
            "type": "Mentor",
            "level": 300,
            "book": 1}

    updated_role = {"name": "Hagrid Hagridson",
            "type": "Mentor of plants",
            "level": 300500,
            "book": 2}

    role_id = create_obj(url_roles, role)
    print('Created. ID = ', role_id)
    print('Get obj by id: ', get_by_id(url_roles, role_id))
    print('Object in list:', get_in_list(url_roles, get_by_id(url_roles, role_id)))
    print('Update object status:', edit_obj(url_roles, role_id, updated_role))
    print('Update status: ', assure_updated(url_roles, updated_role, role_id))
    print('Object in list:', get_in_list(url_roles, get_by_id(url_roles, role_id)))

    print('Deletion status: ', delete_obj(url_roles, role_id))
