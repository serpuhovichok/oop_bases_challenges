"""
У нас есть класс UserManager, который содержит в себе спискок юзернэймов пользователей и может расширять этот список.

Задания:
    1. Создайте класс AdminManager, который будет наследником UserManager.
       У него должен быть свой уникальный метод ban_username, который по переданному в него юзернэйму будет удалять
       юзернэйм из списка. Если такого юзернэйма в списке нет - должно печататься сообщение: "Такого пользователя не существует."
    2. Создайте класс SuperAdminManager, который будет наследником AdminManager.
       У него должен быть свой уникальный метод ban_all_users, который будет удалять все юзернэймы из списка.
    3. Создайте экземпляры каждого из трех классов и у каждого экземпляра вызовите все возможные методы.
"""


class UserManager:
    def __init__(self):
        self.usernames = []

    def add_user(self, username):
        self.usernames.append(username)

    def get_users(self):
        return self.usernames


class AdminManager(UserManager):
    def ban_username(self, username: str) -> None:
        if username not in self.usernames:
            print("Такого пользователя не существует.")
            return

        self.usernames.remove(username)


class SuperAdminManager(AdminManager):
    def ban_all_users(self) -> None:
        self.usernames.clear()


if __name__ == '__main__':
    manager = UserManager()
    manager.add_user(username='Иван')
    print(manager.get_users())

    admin = AdminManager()
    admin.add_user(username='Пётр')
    admin.add_user(username='Феврония')
    print(admin.get_users())
    admin.ban_username('Пётр')
    admin.ban_username('Пётр')

    super_admin = SuperAdminManager()
    super_admin.add_user(username='Пётр')
    super_admin.add_user(username='Феврония')
    print(super_admin.get_users())
    super_admin.ban_all_users()
    super_admin.ban_username('Пётр')

