class GenericConfigs:

    ADMIN = {
        "username" : "Admin",
        "password" : "Admin"
    }
    
    VALID_USER = {
        "username" : "Miki",
        "email" : "miki@test.com",
        "password" : "Miki"
    }

    LOGIN_SUCCESS_MSG = "Welcome back!"
    LOGIN_INVAILD_CREDENCIAL_ERR_MSG = "Password or username is incorrect"

    LOGOUT_SUCCESS_MSG = "You logged out"

    REGISTER_EMPTY_USERNAME_ERR_MSG = "No username was given"
    REGISTER_EMPTY_EMAIL_ERR_MSG = "No email was given"
    REGISTER_INVALID_EMAIL_ERR_MSG = "Email must be valid"
    REGISTER_EMPTY_PASSWORD_ERR_MSG = "No password was given"

    NEW_SITE_POST_MSG = "New place is registered!"
    
    SITE_WITHOUT_REVIEW_URL = ("https://belgrade-with-kids.onrender.com/63b55ca691ea338d5a441609")
    SITE_WITH_REVIEW_URL = ("https://belgrade-with-kids.onrender.com/63b41e48ed3831de2edd565f")

    NEW_REVIEW_POST_MSG = "The review is posted!"
    REVIEW_DELETE_MSG = "The review is deleted! "