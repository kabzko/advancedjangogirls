import React, { useState } from "react";
import { useParams, useNavigate } from "react-router-dom";

import * as api from "../api/api";

import CommentForm from "../components/CommentForm";

function CommentManagePage() {
    const { id } = useParams();
    const navigate = useNavigate();
    const [errors, setErrors] = useState({});
    const [comment, setComment] = useState({
        id: null,
        post: id,
        author: "",
        text: "",
    })

    function handleChange({target}) {
        const updatedPosts = {...comment, [target.name]: target.value};
        setComment(updatedPosts);
    }

    function formIsValid() {
        const _errors = {};
        if (!comment.author) _errors.author = "Author is required";
        if (!comment.text) _errors.text = "Text is required";
        setErrors(_errors);
        return Object.keys(_errors).length === 0;
    }

    function handleSubmit(event) {
        event.preventDefault();
        if (!formIsValid()) return;
        api.createComment(comment).then(() => {
            navigate(`/react/post/${id}`);
        })
    }

    return (
        <div className="container">
            <CommentForm
                errors={errors}
                post={comment} 
                onChange={handleChange} 
                onSubmit={handleSubmit}
            />
        </div>
    );
}

export default CommentManagePage;