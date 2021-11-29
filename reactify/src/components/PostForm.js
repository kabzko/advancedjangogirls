import React from "react";
import TextInput from "./common/TextInput";
import TextArea from "./common/TextArea";
import Button from "./common/Button";

function PostForm(props) {
    return (
        <>
            <form onSubmit={props.onSubmit}>
                <TextInput 
                    id="title"
                    type="text"
                    name="title"
                    label="Title"
                    onChange={props.onChange}
                    value={props.post.title}
                    error={props.errors.title}
                />
                <TextArea
                    id="text"
                    name="text"
                    label="Text"
                    onChange={props.onChange}
                    value={props.post.text}
                    error={props.errors.text}
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

export default PostForm;