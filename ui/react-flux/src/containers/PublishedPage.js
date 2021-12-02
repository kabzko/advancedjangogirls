import React, { useState, useEffect } from "react";

import store from "../stores/stores";

import { getPostsFilteredPublished } from "../actions/actions";

import PostList from "../components/PostList";

function PublishedPage() {
    const [posts, setPosts] = useState(store.getPublishedPosts())

    useEffect(() => {
        store.addChangeListener(onChange);
        if (store.getPublishedPosts().length === 0) getPostsFilteredPublished();
        return () => store.removeChangeListener(onChange);
    }, [])

    function onChange() {
        setPosts(store.getPublishedPosts());
    }

    return (
        <div className="container">
            <PostList posts={posts} />
        </div>
    );
}

export default PublishedPage;