import { handleResponse, handleError } from "./utils";
import axios from "axios";

const api = axios.create({
    baseURL: "/api/"
})

api.interceptors.request.use(config => {
    const token = "token 5eba7f61a8763893aafb0c1b91b475fc1361b695";
    config.headers.Authorization =  token;
    return config;
});

export async function getPostsFilteredPublished() {
    try {
        const response = await api.get("/post/");
        return handleResponse(response);
    } catch (error) {
        return handleError(error);
    }
}

export async function getPostsFilteredUnpublished() {
    try {
        const response = await api.get("/post/draft/");
        return handleResponse(response);
    } catch (error) {
        return handleError(error);
    }
}

export async function getPost(id) {
    try {
        const response = await api.get(`/post/${id}/`);
        return handleResponse(response);
    } catch (error) {
        return handleError(error);
    }
}

export async function savePost(data) {
    try {
        let response = "";
        if (data.id)
            response = await api.put(`/post/${data.id}/`, data);
        else
            response = await api.post(`/post/draft/`, data);
        return handleResponse(response);
    } catch (error) {
        return handleError(error);
    }
}

export async function patchPost(data) {
    try {
        const response = await api.patch(`/post/${data.id}/`, data);
        return handleResponse(response);
    } catch (error) {
        return handleError(error);
    }
}

export async function deletePost(id) {
    try {
        const response = await api.delete(`/post/${id}/`);
        return handleResponse(response);
    } catch (error) {
        return handleError(error);
    }
}

export async function createComment(data) {
    try {
        const response = await api.post(`/comment/`, data);
        return handleResponse(response);
    } catch (error) {
        return handleError(error);
    }
}

export async function patchComment(data) {
    try {
        const response = await api.patch(`/comment/${data.id}/`, data);
        return handleResponse(response);
    } catch (error) {
        return handleError(error);
    }
}

export async function deleteComment(id) {
    try {
        const response = await api.delete(`/comment/${id}/`);
        return handleResponse(response);
    } catch (error) {
        return handleError(error);
    }
}

export async function login(data) {
    try {
        const response = await api.post(`api-token-auth/login/`, data);
        return handleResponse(response);
    } catch (error) {
        return handleError(error);
    }
}