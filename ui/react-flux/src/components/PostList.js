import React from "react";
import { Link } from "react-router-dom";

function PostList(props) {
    function RenderRow() {
        return props.posts.map((post, index) => {
            return (
                <div className="post" key={index}>
                    <Link to={`/react_flux/post/${post.id}`}>
                        <time className="date">{post.published_date}</time>
                        <h2>{post.title}</h2>
                        <p>{post.text}</p>
                        {
                            post.published_date ? <span>Comments: {post.comments_count}</span>
                            : null
                        }
                    </Link>
                </div>
            )
        })
    }

    return (
        <>
            {RenderRow()}
        </>
    );
}

export default PostList;