import React from "react";
import { Routes, Route } from "react-router-dom";
import { useNavigate } from "react-router-dom";

import * as api from "../api/api";

import NotFoundPage from "./NotFoundPage";
import PublishedPage from "./PublishedPage";
import UnpublishedPage from "./UnpublishedPage";
import DetailPage from "./DetailPage";
import PostManagePage from "./PostManagePage";
import CommentManagePage from "./CommentManagePage";
import LoginPage from "./LoginPage";

import Header from "../components/common/Header";

function App() {
    const navigate = useNavigate();

    function logout() {
        api.logout().then(() => {
            localStorage.clear();
            navigate('/react_flux');
        });
    }

    return (
        <>
            <Header 
                title="Django Girls Blog"
                onClick={logout}
            />
            <Routes>
                <Route path="/react_flux/*" element={<NotFoundPage />} />
                <Route path="/react_flux/" element={<PublishedPage />} />
                <Route path="/react_flux/post/draft" element={<UnpublishedPage />} />
                <Route path="/react_flux/post/:id" element={<DetailPage />} />
                <Route path="/react_flux/post/new" element={<PostManagePage />} />
                <Route path="/react_flux/post/edit/:id" element={<PostManagePage />} />
                <Route path="/react_flux/comment/:id" element={<CommentManagePage />} />
                <Route path="/react_flux/login" element={<LoginPage />} />
            </Routes>
        </>
    );
}

export default App;
