from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task

# The 'home' route: This function handles requests to the home page ('/').
# It queries the database for all tasks in the 'Task' table, orders them by 'id', 
# and passes the task list to the 'tasks.html' template to be rendered.
@app.route("/")
def home():
    tasks = list(Task.query.order_by(Task.id).all())  # Fetch all tasks, ordered by their ID.
    return render_template("tasks.html", tasks=tasks)  # Pass the task list to the template.

# The 'categories' route: This route handles requests to the '/categories' URL.
# It queries the 'Category' table for all categories, orders them alphabetically 
# by 'category_name', and sends this list to the 'categories.html' template for rendering.
@app.route("/categories")
def categories():
    categories = list(Category.query.order_by(Category.category_name).all())  # Fetch all categories.
    return render_template("categories.html", categories=categories)  # Pass the categories to the template.

# The 'add_category' route: Handles both GET and POST requests for adding a new category.
# If a POST request is received (when a user submits the form), it retrieves the 'category_name'
# from the form, creates a new 'Category' object, adds it to the database, and commits the change.
# If the request is a GET (loading the form), it simply renders the 'add_category.html' page.
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":  # Check if the form is submitted (POST request).
        # Create a new Category object from the form input.
        category = Category(category_name=request.form.get("category_name"))  
        db.session.add(category)  # Add the new category to the session (staging area).
        db.session.commit()  # Commit the change to the database.
        return redirect(url_for("categories"))  # Redirect to the categories list after adding the new one.
    return render_template("add_category.html")  # Render the form if it's a GET request.

# The 'edit_category' route: Handles the logic for editing an existing category.
# When the user navigates to this route, it first retrieves the category by 'category_id'.
# If the request is POST (form submission), it updates the category's name, commits the changes,
# and redirects back to the categories list. If it's a GET request, it loads the current category 
# into the form for editing.
@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)  # Retrieve category by ID or return 404 if not found.
    if request.method == "POST":  # Check if the form was submitted (POST request).
        category.category_name = request.form.get("category_name")  # Update the category name.
        db.session.commit()  # Commit the changes to the database.
        return redirect(url_for("categories"))  # Redirect to categories page.
    return render_template("edit_category.html", category=category)  # Render form with existing category data.

# The 'delete_category' route: Handles deletion of categories.
# It takes the category's ID as a parameter, retrieves the corresponding category from the database,
# deletes it, commits the deletion, and then redirects back to the categories page.
@app.route("/delete_category/<int:category_id>")
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)  # Retrieve the category by ID, return 404 if not found.
    db.session.delete(category)  # Mark the category for deletion.
    db.session.commit()  # Commit the deletion to the database.
    return redirect(url_for("categories"))  # Redirect to categories page after deletion.

# The 'add_task' route: This route handles both GET and POST requests for adding a new task.
# It queries the categories list for the dropdown menu (so the task can be assigned a category).
# When the form is submitted (POST), it retrieves the form data, creates a new 'Task' object,
# and adds it to the database. Finally, it redirects to the home page.
@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    categories = list(Category.query.order_by(Category.category_name).all())  # Fetch all categories for the form.
    if request.method == "POST":  # Handle form submission.
        task = Task(
            task_name=request.form.get("task_name"),  # Retrieve the task name from the form.
            task_description=request.form.get("task_description"),  # Retrieve task description.
            is_urgent=bool(True if request.form.get("is_urgent") else False),  # Convert the urgency checkbox to a boolean.
            due_date=request.form.get("due_date"),  # Get the task's due date.
            category_id=request.form.get("category_id")  # Get the category ID selected by the user.
        )
        db.session.add(task)  # Add the new task to the session (staging).
        db.session.commit()  # Commit the new task to the database.
        return redirect(url_for("home"))  # Redirect back to the home page where all tasks are listed.
    return render_template("add_task.html", categories=categories)  # Render the 'add_task.html' form with categories.

# The 'edit_task' route: This route allows the user to edit an existing task.
# It first retrieves the task to be edited by its ID, as well as all categories for the dropdown list.
# If the form is submitted (POST), it updates the task fields and commits the changes.
@app.route("/edit_task/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)  # Retrieve task by ID or return 404 if not found.
    categories = list(Category.query.order_by(Category.category_name).all())  # Fetch categories for dropdown.
    if request.method == "POST":  # Handle form submission.
        task.task_name = request.form.get("task_name")  # Update task name.
        task.task_description = request.form.get("task_description")  # Update task description.
        task.is_urgent = bool(True if request.form.get("is_urgent") else False)  # Update urgency status.
        task.due_date = request.form.get("due_date")  # Update due date.
        task.category_id = request.form.get("category_id")  # Update the category ID.
        db.session.commit()  # Commit the changes to the database.
    return render_template("edit_task.html", task=task, categories=categories)  # Render form with task and categories data.

# The 'delete_task' route: Handles the deletion of a task.
# It takes the task ID as a parameter, retrieves the corresponding task from the database, deletes it,
# commits the change, and then redirects to the home page where all tasks are displayed.
@app.route("/delete_task/<int:task_id>")
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)  # Retrieve the task by ID or return 404 if not found.
    db.session.delete(task)  # Mark the task for deletion.
    db.session.commit()  # Commit the deletion to the database.
    return redirect(url_for("home"))  # Redirect back to the home page after task deletion.
