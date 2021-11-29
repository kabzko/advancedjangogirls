import React, { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";

import * as api from "../api/api";

import PostDetail from "../components/PostDetail";

function DetailPage() {
    const { id } = useParams();
    const navigate = useNavigate();
    const [post, setPost] = useState({
        comments: [],
        comments_count: "",
        created_date: "",
        id: "",
        published_date: "",
        text: "",
        title: "",
    })

    useEffect(() => {
        api.getPost(id).then(response => {
            setPost(response);
        })
    }, [id])

    function publishPost() {
        const data = {"id": id ,"action": "publish"}
        api.patchPost(data).then(() => {
            navigate('/react');
        })
    }

    function deletePost() {
        api.deletePost(id).then(() => {
            navigate('/react/post/draft');
        })
    }

    function approveComment(comment_id) {
        console.log(comment_id)
        const data = {"id": comment_id ,"action": "approve"}
        api.patchComment(data).then(() => {
            navigate('/react');
        })
    }

    function removeComment(comment_id) {
        api.deleteComment(comment_id).then(() => {
            navigate(`/react/post/${id}`);
        })
    }

    return (
        <div className="container">
            <PostDetail 
                post={post} 
                publishClick={publishPost} 
                deleteClick={deletePost} 
                approveClick={approveComment}
                removeClick={removeComment}
            />
        </div>
    );
}

export default DetailPage;