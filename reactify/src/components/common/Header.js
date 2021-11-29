import React from "react";
import { Link } from "react-router-dom";

function Header(props) {
    return (
        <header className="page-header">
            <div className="container">
                <Link to="/react/post/draft" className="top-menu">
                    <span className="glyphicon glyphicon-edit"></span>
                </Link>
                <Link to="/react/post/new" className="top-menu">
                    <span className="glyphicon glyphicon-plus"></span>
                </Link>
                <p className="top-menu">
                Hello 
                <small>(<Link to="">Log out</Link>)</small>
                </p>
                <Link to="" className="top-menu">
                    <span className="glyphicon glyphicon-lock"></span>
                </Link>
                <h1>
                    <Link to="/react">{props.title}</Link>
                </h1>
            </div>
        </header>
    );
}

export default Header;