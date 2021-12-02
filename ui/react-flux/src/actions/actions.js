import dispatcher from "../appDispatcher";
import * as api from "../api/api";
import actionTypes from "./actionTypes";

export function getPostsFilteredPublished() {
    return api.getPostsFilteredPublished().then(posts => {
        dispatcher.dispatch({
            actionType: actionTypes.LOAD_POSTS_PUBLISHED,
            posts: posts
        });
    })
}

export function getPostsFilteredUnpublished() {
    return api.getPostsFilteredUnpublished().then(posts => {
        dispatcher.dispatch({
            actionType: actionTypes.LOAD_POSTS_UNPUBLISH,
            posts: posts
        });
    })
}

export function getPostById(id) {
    return api.getPostById(id).then(post => {
        dispatcher.dispatch({
            actionType: actionTypes.LOAD_POST_BY_ID,
            post: post
        });
    })
}

export function savePost(post) {
    return api.savePost(post).then(savedPost => {
        dispatcher.dispatch({
            actionType: post.id ? actionTypes.UPDATE_POST : actionTypes.CREATE_POST,
            post: savedPost.record
        });
    })
}

export function patchPost(post) {
    return api.patchPost(post).then(publishedPost => {
        dispatcher.dispatch({
            actionType: actionTypes.PUBLISH_POST,
            post: publishedPost.record
        });
    })
}

export function deletePost(id) {
    return api.deletePost(id).then(() => {
        dispatcher.dispatch({
            actionType: actionTypes.DELETE_POST,
            id: id
        });
    })
}

export function createComment(comment) {
    return api.createComment(comment).then(savedComment => {
        dispatcher.dispatch({
            actionType: actionTypes.CREATE_COMMENT,
            post: savedComment.record
        });
    })
}

export function patchComment(comment) {
    return api.patchComment(comment).then(approvedComment => {
        dispatcher.dispatch({
            actionType: actionTypes.APPROVE_COMMENT,
            post: approvedComment.record
        });
    })
}

export function deleteComment(id) {
    return api.deleteComment(id).then(() => {
        dispatcher.dispatch({
            actionType: actionTypes.DELETE_COMMENT,
            id: id
        });
    })
}

export function login(credential) {
    return api.login(credential).then(authentication => {
        dispatcher.dispatch({
            actionType: actionTypes.LOGIN,
            authentication: authentication
        });
    })
}