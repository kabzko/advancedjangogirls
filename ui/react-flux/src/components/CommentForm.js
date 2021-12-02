import React from "react";
import TextInput from "./common/TextInput";
import TextArea from "./common/TextArea";
import Button from "./common/Button";

function CommentForm(props) {
    return (
        <>
            <form onSubmit={props.onSubmit}>
                <TextInput 
                    id="author"
                    name="author"
                    label="Author"
                    onChange={props.onChange}
                    value={props.post.author}
                    error={props.errors.author}
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

export default CommentForm;