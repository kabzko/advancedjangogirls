import React, { useState, useEffect } from "react";
import { useParams, useNavigate, useLocation } from "react-router-dom";

import store from "../stores/stores";

import { getPostById, savePost, getPostsFilteredUnpublished } from "../actions/actions";

import PostForm from "../components/PostForm";

function PostManagePage() {
    const { id } = useParams();
    const { pathname } = useLocation();
    const navigate = useNavigate();
    const [errors, setErrors] = useState({});
    const [post, setPost] = useState([])

    useEffect(() => {
        if (pathname === "/react_flux/post/new") {
            setPost({
                id: null,
                author: "2",
                title: "",
                text: "",
            });
            getPostsFilteredUnpublished();
        } else {
            store.addChangeListener(onChange);
            if (post.length === 0) {
                getPostById(id)
            } else if (id) {
                setPost(getPostById(id));
            }
            return () => store.removeChangeListener(onChange);
        }
    }, [post.length, pathname, id])

    function onChange() {
        setPost(store.getPostById());
    }

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
        savePost(post).then(() => {
            navigate('/react_flux/post/draft');
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