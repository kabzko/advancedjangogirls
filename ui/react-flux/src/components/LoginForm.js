import React from "react";
import TextInput from "./common/TextInput";
import Button from "./common/Button";

function LoginForm(props) {
    return (
        <>
            <form onSubmit={props.onSubmit}>
                <TextInput 
                    id="username"
                    type="text"
                    name="username"
                    label="Username"
                    onChange={props.onChange}
                    value={props.credentials.username}
                    error={props.errors.username}
                />
                <TextInput
                    id="password"
                    type="password"
                    name="password"
                    label="Password"
                    onChange={props.onChange}
                    value={props.credentials.password}
                    error={props.errors.password}
                />
                <Button
                    id="button"
                    name="button"
                    type="submit"
                    label="Submit"
                />
            </form>
        </>
    );
}

export default LoginForm;