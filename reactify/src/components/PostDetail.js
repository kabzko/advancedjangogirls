import React from "react";
import { Link } from "react-router-dom";

function PostDetail(props) {

    function renderComment() {
        return props.post.comments.map(comment => {
            return(
                <div key={comment.id} className="comment">
                    {
                        comment.approved_comment ?
                        null : <div className="date">
                            <span>{comment.created_date}</span>
                            <button className="btn btn-default" onClick={() => props.removeClick(comment.id)}>
                                <span className="glyphicon glyphicon-remove"></span>
                            </button>
                            <button className="btn btn-default" onClick={() => props.approveClick(comment.id)}>
                                <span className="glyphicon glyphicon-ok"></span>
                            </button>
                        </div>
                    }
                    <strong>{comment.author}</strong>
                    <p>{comment.text}</p>
                </div>
            )
        })
    }

    return (
        <div className="post">
            {
                props.post.published_date ? 
                null : <aside className="actions">
                    <Link to={`/react/post/edit/${props.post.id}`} className="btn btn-default">
                        <span className="glyphicon glyphicon-pencil"></span>
                    </Link>
                    <button className="btn btn-default" onClick={props.deleteClick}>
                        <span className="glyphicon glyphicon-remove"></span>
                    </button>
                </aside>
            }
            <div className="date mx-2">
                {props.post.published_date}
            </div>
            {
                props.post.published_date ? 
                null : <button className="btn btn-default" onClick={props.publishClick}>Publish</button>
            }
            <h2>{props.post.title}</h2>
            <p>{props.post.text}</p>
            <hr />
            {
                props.post.published_date ? 
                props.post.comments.length > 0 ? 
                renderComment() : <p>No comments here yet!</p> 
                : null
            }
            {
                props.post.published_date ? 
                <Link to={`/react/comment/${props.post.id}`} className="btn btn-default">Add Comment</Link> : null
            }
        </div>
    );
}

export default PostDetail;