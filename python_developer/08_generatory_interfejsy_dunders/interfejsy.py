class User:
    def __init__(self, name, age, balance, groups):
        """
        Initialize the User object with a name, age, balance, and a dictionary of groups with permissions.
        name: user's name (string)
        age: user's age (integer)
        balance: user's account balance (float)
        groups: dictionary where the key is a group name, and the value is a list of permissions (dict)
        """
        self.name = name
        self.age = age
        self.balance = balance
        self.groups = groups

    def __int__(self):
        """Called when int() is used on an instance of the class. Returns user's age."""
        return self.age

    def __float__(self):
        """Called when float() is used on an instance of the class. Returns user's balance."""
        return self.balance

    def __str__(self):
        """Called when str() is used on an instance of the class. Returns user's name and details."""
        return f"User(name={self.name}, age={self.age}, balance={self.balance}, groups={self.groups})"

    def __bool__(self):
        """Called when bool() is used on an instance of the class. Returns True if the user is active (has balance)."""
        return self.balance > 0

    def __len__(self):
        """Called when len() is used on an instance of the class. Returns the number of groups."""
        return len(self.groups)

    def __getitem__(self, group):
        """Called when accessing a group via indexing (e.g., user['adminpanel'])."""
        return self.groups[group]

    def __setitem__(self, group, permissions):
        """Called when setting permissions for a group (e.g., user['adminpanel'] = ['read', 'write'])."""
        self.groups[group] = permissions

    def __rshift__(self, other_user):
        """Copy groups and permissions from the current user to another user."""
        other_user.groups = {
            group: perms.copy() for group, perms in self.groups.items()
        }
        print(
            f"Groups and permissions from {self.name} have been copied to {other_user.name}"
        )


# Example usage:

user1 = User(
    name="Kuba",
    age=30,
    balance=150.75,
    groups={
        "data_warehouse": ["read", "write"],
        "intranet": ["read"],
        "email": ["send", "receive"],
        "adminpanel": ["full_access"],
    },
)

user2 = User(
    name="Ola",
    age=28,
    balance=250.00,
    groups={
        "data_warehouse": ["read"],
        "intranet": ["read"],
        "email": ["send"],
        "adminpanel": [],
    },
)


# Print the user objects
print(user1)
print(user2)


# __int__ and __float__
print(int(user1))  # Output: 30 (user's age)
print(float(user1))  # Output: 150.75 (user's balance)

# __str__
print(
    str(user1)
)  # Output: User(name=Kuba, age=30, balance=150.75, groups={'data_warehouse': ['read', 'write'], 'intranet': ['read'], 'email': ['send', 'receive'], 'adminpanel': ['full_access']})

# __bool__
print(bool(user1))  # Output: True (since balance is > 0)

# __len__
print(len(user1))  # Output: 4 (number of groups)

# __getitem__ and __setitem__
print(
    user1["adminpanel"]
)  # Output: ['full_access'] (get permissions for 'adminpanel' group)

user1["adminpanel"] = ["view only"]  # Update permissions for 'adminpanel' group
print(user1["adminpanel"])  # Output: ['view only'] (updated permissions)

# Copy groups and permissions using >>
user1 >> user2

# Check user2's updated groups and permissions
print(user2.groups)
# Output:
# {
#   'data_warehouse': ['read', 'write'],
#   'intranet': ['read'],
#   'email': ['send', 'receive'],
#   'adminpanel': ['view only']
# }


# Print the user objects
print(user1)
print(user2)
