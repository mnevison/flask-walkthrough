from taskmanager import db


# Category Model: This class represents the 'Category' table in the database.
# It defines the schema for storing task categories, and has a one-to-many 
# relationship with the 'Task' model (one category can have many tasks).
class Category(db.Model):
    # 'id' is the primary key of the Category table. It's an auto-incrementing integer.
    id = db.Column(db.Integer, primary_key=True)

    # 'category_name' is a string column with a maximum length of 25 characters.
    # It must be unique (no two categories can have the same name), and cannot be null.
    category_name = db.Column(db.String(25), unique=True, nullable=False)

    # 'tasks' defines the relationship with the 'Task' model. It's a one-to-many relationship,
    # meaning one category can have many tasks. The 'backref' allows you to access the category
    # from the 'Task' model, and 'lazy=True' loads tasks only when needed.
    # 'cascade="all, delete"' ensures that when a category is deleted, all its related tasks are deleted too.
    tasks = db.relationship("Task", backref="category", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ provides a string representation of the Category object.
        # When printed, this will return the category's name, making it more readable in the console.
        return self.category_name


# Task Model: This class represents the 'Task' table in the database.
# It defines the schema for storing tasks, including the task details and its relationship with categories.
class Task(db.Model):
    # 'id' is the primary key of the Task table. It's an auto-incrementing integer.
    id = db.Column(db.Integer, primary_key=True)

    # 'task_name' is a string column with a maximum length of 50 characters.
    # Like category_name, it must be unique (no two tasks can have the same name) and cannot be null.
    task_name = db.Column(db.String(50), unique=True, nullable=False)

    # 'task_description' is a text column for the detailed description of the task.
    # This field is required and cannot be null.
    task_description = db.Column(db.Text, nullable=False)

    # 'is_urgent' is a boolean column that indicates whether the task is urgent or not.
    # By default, this value is set to 'False'. It cannot be null, ensuring a value is always provided.
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)

    # 'due_date' is a date column that stores the task's due date.
    # This field is required and cannot be null.
    due_date = db.Column(db.Date, nullable=False)

    # 'category_id' establishes the foreign key relationship between the Task and Category tables.
    # Each task is associated with a specific category, and 'ondelete="CASCADE"' ensures that if 
    # the category is deleted, all associated tasks will also be deleted.
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ provides a string representation of the Task object.
        # It displays the task ID, task name, and whether it's urgent.
        # Useful for debugging and displaying task details in the console.
        return "#{0} - Task: {1} | Urgent: {2}".format(
            self.id, self.task_name, self.is_urgent
        )
