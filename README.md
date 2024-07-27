# To-Do List Application

## Overview

This To-Do List application is a simple and interactive tool designed to help users manage their tasks efficiently. It is built using the Flet framework, which allows for building web, desktop, and mobile applications with a single codebase. The application includes features such as adding, viewing, and managing tasks with an intuitive user interface.

## Author

Created By: ScriptPythonic

## Features

- **Add Tasks**: Users can add new tasks with descriptions.
- **View Tasks**: All added tasks are displayed in a list with the creation date and time.
- **Delete/Edit Tasks**: Users can delete or edit tasks (functionality not implemented in this version).
- **Responsive UI**: The application interface is designed to be responsive and user-friendly.

## Prerequisites

- Python 3.8 or higher
- Flet framework

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/ScriptPythonic/todo-list-app.git
    cd todo-list-app
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the application**:
    ```bash
    python main.py
    ```

2. **Access the application**:
    Open your browser and go to `http://0.0.0.0:8000` to view the To-Do List application.

## Code Structure

### `FormContainer` Class

This class defines a form container for adding tasks. It includes a text field for the task description and a button to add the task.

- **`__init__`**: Initializes the form container with a function to handle task addition.
- **`build`**: Builds the UI components for the form container.

### `CreateTask` Class

This class defines a task container for displaying tasks. It includes the task description and creation date.

- **`__init__`**: Initializes the task container with the task description and date.
- **`TaskDeleteEdit`**: Creates a button for deleting or editing a task.
- **`build`**: Builds the UI components for the task container.

### `main` Function

This function sets up the main page and handles interactions.

- **`AddTaskToScreen`**: Adds a task to the screen.
- **`CreateToDoTask`**: Toggles the visibility of the form container.
- **Main Container**: Constructs the main container and adds it to the page.
- **Final Page Setup**: Updates the page and assigns the form container.

### Main Block

Starts the application if the script is executed directly.

## Contributing

1. **Fork the repository**.
2. **Create a new branch**:
    ```bash
    git checkout -b feature-name
    ```
3. **Commit your changes**:
    ```bash
    git commit -m 'Add some feature'
    ```
4. **Push to the branch**:
    ```bash
    git push origin feature-name
    ```
5. **Create a new Pull Request**.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Flet framework for providing an easy-to-use and powerful tool for building the UI.
- Python for being the core language of the project.

---

Feel free to customize this README to better suit your project's specific details and structure.
