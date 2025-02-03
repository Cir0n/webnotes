from app.models.user import UserModel

def create_admin():
    username = input("Enter username: ")
    password = input("Enter password: ")

    user_model = UserModel()
    admin_id = user_model.add_admin(username, password)

    print(f"Admin created with id: {admin_id}")


if __name__ == "__main__":
    create_admin()