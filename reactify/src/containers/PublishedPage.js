import React, { useState, useEffect } from "react";

import * as api from "../api/api";

import PostList from "../components/PostList";

function PublishedPage() {
    const [posts, setPosts] = useState([])

    useEffect(() => {
        api.getPostsFilteredPublished().then(response => {
            setPosts(response);
        })
    }, [])

    return (
        <div className="container">
            <PostList posts={posts} />
        </div>
    );
}

export default PublishedPage;