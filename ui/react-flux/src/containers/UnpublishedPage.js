import React, { useState, useEffect } from "react";

import store from "../stores/stores";

import { getPostsFilteredUnpublished } from "../actions/actions";

import PostList from "../components/PostList";

function PublishedPage() {
    const [posts, setPosts] = useState(store.getUnpublishedPosts())

    useEffect(() => {
        store.addChangeListener(onChange);
        if (store.getUnpublishedPosts().length === 0) {
            getPostsFilteredUnpublished();
        }
        return () => store.removeChangeListener(onChange);
    }, [])

    function onChange() {
        setPosts(store.getUnpublishedPosts());
    }

    return (
        <div className="container">
            <PostList posts={posts} />
        </div>
    );
}

export default PublishedPage;