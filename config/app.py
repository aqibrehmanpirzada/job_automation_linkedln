from flask import Flask, request, render_template_string
import config_config_secrets  # Update to the new file name

app = Flask(__name__)

# Path to the file where credentials are stored
CONFIG_FILE = "config_config_secrets.py"  # Updated filename to config_secrets.py

# HTML form template with embedded CSS
form_html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Update Credentials</title>
  <style>
    body {
      font-family: 'Arial', sans-serif;
      background: linear-gradient(to bottom right, #6a11cb, #2575fc);
      color: #fff;
      margin: 0;
      padding: 0;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }
    .container {
      background: rgba(255, 255, 255, 0.1);
      padding: 20px 40px;
      border-radius: 10px;
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
      text-align: center;
      max-width: 400px;
      width: 100%;
    }
    h1 {
      margin-bottom: 20px;
      font-size: 24px;
      color: #ffffff;
    }
    label {
      display: block;
      margin: 10px 0 5px;
      font-size: 14px;
      color: #fff;
    }
    input {
      width: 100%;
      padding: 10px;
      margin-bottom: 20px;
      border: none;
      border-radius: 5px;
      outline: none;
    }
    input[type="email"],
    input[type="password"] {
      background: rgba(255, 255, 255, 0.2);
      color: #fff;
    }
    button {
      padding: 10px 20px;
      background: #ff6b6b;
      color: #fff;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      font-size: 16px;
    }
    button:hover {
      background: #ff4757;
    }
    @media screen and (max-width: 768px) {
      .container {
        padding: 15px 30px;
      }
      h1 {
        font-size: 20px;
      }
      button {
        font-size: 14px;
      }
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Update Login Credentials</h1>
    <form action="/update_credentials" method="POST">
      <label for="username">Username:</label>
      <input type="email" id="username" name="username" required placeholder="Enter your email">
      <label for="password">Password:</label>
      <input type="password" id="password" name="password" required placeholder="Enter your password">
      <button type="submit">Update</button>
    </form>
  </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(form_html)

@app.route('/update_credentials', methods=['POST'])
def update_credentials():
    # Get form data
    new_username = request.form['username']
    new_password = request.form['password']
    
    # Read the file and update credentials
    with open(CONFIG_FILE, 'r') as file:
        lines = file.readlines()
    
    # Replace username and password in the file
    with open(CONFIG_FILE, 'w') as file:
        for line in lines:
            if line.strip().startswith("username ="):
                file.write(f'username = "{new_username}"       # Enter your username in the quotes\n')
            elif line.strip().startswith("password ="):
                file.write(f'password = "{new_password}"           # Enter your password in the quotes\n')
            else:
                file.write(line)
    
    return "Credentials updated successfully!"

if __name__ == '__main__':
    app.run(debug=True)
