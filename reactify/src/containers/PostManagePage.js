import React, { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";

import * as api from "../api/api";

import PostForm from "../components/PostForm";

function PostManagePage() {
    const { id } = useParams();
    const navigate = useNavigate();
    const [errors, setErrors] = useState({});
    const [post, setPost] = useState({
        id: null,
        author: "2",
        title: "",
        text: "",
    })

    useEffect(() => {
        if (id) {
            api.getPost(id).then(response => {
                setPost(response);
            })
        }
    }, [id])

    function handleChange({target}) {
        const updateInputed = {...post, [target.name]: target.value};
        setPost(updateInputed);
    }

    function formIsValid() {
        const _errors = {};
        if (!post.title) _errors.title = "Title is required";
        if (!post.text) _errors.text = "Text is required";
        setErrors(_errors);
        return Object.keys(_errors).length === 0;
    }

    function handleSubmit(event) {
        event.preventDefault();
        if (!formIsValid()) return;
        api.savePost(post).then(() => {
            navigate('/react/post/draft');
        })
    }

    return (
        <div className="container">
            <PostForm
                errors={errors}
                post={post} 
                onChange={handleChange} 
                onSubmit={handleSubmit}
            />
        </div>
    );
}

export default PostManagePage;