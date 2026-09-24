from src.utils.validate import validate_name


def setup_mantap():
    print("Setting up Mantap versi A dan B...")


def register_user(name):
    if not validate_name(name):
        print("Nama tidak valid: tidak boleh kosong")
        return False
    print(f"User {name} terdaftar")
    return True


if __name__ == "__main__":
    setup_mantap()
    register_user("")
    register_user("Billy")