import React from "react";
import TextInput from "./common/TextInput";
import TextArea from "./common/TextArea";
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
                    value={props.post.username}
                    error={props.errors.username}
                />
                <TextArea
                    id="password"
                    name="password"
                    label="Password"
                    onChange={props.onChange}
                    value={props.post.password}
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