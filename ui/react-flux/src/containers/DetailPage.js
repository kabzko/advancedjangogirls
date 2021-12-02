import React, { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";

import store from "../stores/stores";

import { getPostById, patchPost, deletePost, patchComment, deleteComment } from "../actions/actions";

import PostDetail from "../components/PostDetail";

function DetailPage() {
    const { id } = useParams();
    const navigate = useNavigate();
    const [post, setPost] = useState(store.getPostById());


    useEffect(() => {
        store.addChangeListener(onChange);
        if (post.length === 0) {
            getPostById(id)
        } else if (id) {
            setPost(getPostById(id));
        }
        return () => store.removeChangeListener(onChange);
    }, [post.length, id])

    function onChange() {
        setPost(store.getPostById());
    }

    function publishPost() {
        const data = {"id": id ,"action": "publish"}
        patchPost(data).then(() => {
            getPostById(id)
            setPost(store.getPostById());
            navigate(`/react_flux/post/${id}`);
        })
    }

    function removePost() {
        deletePost(id).then(() => {
            navigate('/react_flux/post/draft');
        })
    }

    function approveComment(comment_id) {
        const data = {"id": comment_id ,"action": "approve"}
        patchComment(data).then(() => {
            getPostById(id);
            setPost(store.getPostById());
            navigate(`/react_flux/post/${id}`);
        })
    }

    function removeComment(comment_id) {
        deleteComment(comment_id).then(() => {
            getPostById(id);
            setPost(store.getPostById());
            navigate(`/react_flux/post/${id}`);
        })
    }

    return (
        <div className="container">
            <PostDetail 
                post={post} 
                publishClick={publishPost} 
                deleteClick={removePost} 
                approveClick={approveComment}
                removeClick={removeComment}
            />
        </div>
    );
}

export default DetailPage;