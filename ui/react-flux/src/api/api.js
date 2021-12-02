import { handleResponse, handleError } from "./utils";
import axios from "axios";

const api = axios.create({
    baseURL: "/api/"
})

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
        const header = {
            headers: {
                'Authorization': `token ${localStorage.token}` 
            }
        }
        const response = await api.get("/post/draft/", header);
        return handleResponse(response);
    } catch (error) {
        return handleError(error);
    }
}

export async function getPostById(id) {
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
        const header = {
            headers: {
                'Authorization': `token ${localStorage.token}` 
            }
        }
        if (data.id)
            response = await api.put(`/post/${data.id}/`, data, header);
        else
            response = await api.post(`/post/draft/`, data, header);
        return handleResponse(response);
    } catch (error) {
        return handleError(error);
    }
}

export async function patchPost(data) {
    try {
        const header = {
            headers: {
                'Authorization': `token ${localStorage.token}` 
            }
        }
        const response = await api.patch(`/post/${data.id}/`, data, header);
        return handleResponse(response);
    } catch (error) {
        return handleError(error);
    }
}

export async function deletePost(id) {
    try {
        const header = {
            headers: {
                'Authorization': `token ${localStorage.token}` 
            }
        }
        const response = await api.delete(`/post/${id}/`, header);
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
        const header = {
            headers: {
                'Authorization': `token ${localStorage.token}` 
            }
        }
        const response = await api.patch(`/comment/${data.id}/`, data, header);
        return handleResponse(response);
    } catch (error) {
        return handleError(error);
    }
}

export async function deleteComment(id) {
    try {
        const header = {
            headers: {
                'Authorization': `token ${localStorage.token}` 
            }
        }
        const response = await api.delete(`/comment/${id}/`, header);
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

export async function logout() {
    try {
        const header = {
            headers: {
                'Authorization': `token ${localStorage.token}` 
            }
        }
        const response = await api.post(`api-token-auth/logout/`, {}, header);
        return handleResponse(response);
    } catch (error) {
        return handleError(error);
    }
}