import React from "react";
import { Link } from "react-router-dom";

function Header(props) {
    return (
        <header className="page-header">
            <div className="container">
                {
                    localStorage.isLogin ? 
                    <>
                        <Link to="/react_flux/post/draft" className="top-menu">
                            <span className="glyphicon glyphicon-edit"></span>
                        </Link>
                        <Link to="/react_flux/post/new" className="top-menu">
                            <span className="glyphicon glyphicon-plus"></span>
                        </Link>
                        <p className="top-menu">
                            <button className="btn btn-primary" onClick={props.onClick}>Log out</button>
                        </p>
                    </> :
                    <Link to="/react_flux/login" className="top-menu">
                        <span className="glyphicon glyphicon-lock"></span>
                    </Link>
                }
                <h1>
                    <Link to="/react_flux">{props.title}</Link>
                </h1>
            </div>
        </header>
    );
}

export default Header;