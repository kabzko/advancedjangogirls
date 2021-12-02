import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

import * as api from "../api/api";

import store from "../stores/stores";

import LoginForm from "../components/LoginForm";

function LoginPage() {
    const navigate = useNavigate();
    const [errors, setErrors] = useState({});
    const [credentials, setCredentials] = useState({
        username: "",
        password: "",
    })

    function handleChange({target}) {
        const updateInputed = {...credentials, [target.name]: target.value};
        setCredentials(updateInputed);
    }

    function formIsValid() {
        const _errors = {};
        if (!credentials.username) _errors.username = "Username is required";
        if (!credentials.password) _errors.password = "Password is required";
        setErrors(_errors);
        return Object.keys(_errors).length === 0;
    }

    function handleSubmit(event) {
        event.preventDefault();
        if (!formIsValid()) return;
        api.login(credentials).then(response => {
            localStorage.isLogin = true;
            localStorage.token = response.token;
            navigate('/react_flux');
        })
    }

    return (
        <div className="container">
            <LoginForm
                errors={errors}
                credentials={credentials}
                onChange={handleChange} 
                onSubmit={handleSubmit}
            />
        </div>
    );
}

export default LoginPage;