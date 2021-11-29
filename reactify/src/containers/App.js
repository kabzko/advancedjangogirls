import React from "react";
import { Routes, Route } from "react-router-dom";

import NotFoundPage from "./NotFoundPage";
import PublishedPage from "./PublishedPage";
import UnpublishedPage from "./UnpublishedPage";
import DetailPage from "./DetailPage";
import PostManagePage from "./PostManagePage";
import CommentManagePage from "./CommentManagePage";

import Header from "../components/common/Header";

function App() {
    return (
        <>
            <Header title="Django Girls Blog" />
            <Routes>
                <Route path="/react/*" element={<NotFoundPage />} />
                <Route path="/react/" element={<PublishedPage />} />
                <Route path="/react/post/draft" element={<UnpublishedPage />} />
                <Route path="/react/post/:id" element={<DetailPage />} />
                <Route path="/react/post/new" element={<PostManagePage />} />
                <Route path="/react/post/edit/:id" element={<PostManagePage />} />
                <Route path="/react/comment/:id" element={<CommentManagePage />} />
            </Routes>
        </>
    );
}

export default App;
