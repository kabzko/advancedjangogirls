import React, { useState } from "react";

import LoginForm from "../components/LoginForm";

function LoginPage() {
    const [credentials, setCredentials] = useState({
        username: "",
        password: "",
    })

    return (
        <div className="container">
            <LoginForm />
        </div>
    );
}

export default LoginPage;