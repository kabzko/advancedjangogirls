import { EventEmitter } from "events";
import Dispatcher from "../appDispatcher";
import actionTypes from "../actions/actionTypes";

const CHANGE_EVENT = "change";
let _publishedposts = [];
let _unpublishedposts = [];
let _post = [];

class Store extends EventEmitter {
    addChangeListener(callback) {
        this.on(CHANGE_EVENT, callback);
    }

    removeChangeListener(callback) {
        this.removeListener(CHANGE_EVENT, callback);
    }

    emitChange() {
        this.emit(CHANGE_EVENT);
    }

    getPublishedPosts() {
        return _publishedposts;
    }

    getUnpublishedPosts() {
        return _unpublishedposts.reverse();
    }

    getPostById() {
        return _post;
    }
}

const store = new Store();

Dispatcher.register(action => {
    switch(action.actionType) {
        case actionTypes.LOAD_POSTS_PUBLISHED:
            _publishedposts = action.posts;
            store.emitChange();
            break;
        case actionTypes.LOAD_POSTS_UNPUBLISH:
            _unpublishedposts = action.posts;
            store.emitChange();
            break;
        case actionTypes.LOAD_POST_BY_ID:
            _post = action.post;
            store.emitChange();
            break;
        case actionTypes.CREATE_POST:
            _unpublishedposts.push(action.post);
            store.emitChange();
            break;
        case actionTypes.UPDATE_POST:
            _unpublishedposts = _unpublishedposts.map(post => 
                post.id === action.post.id ? action.post : post
            );
            store.emitChange();
            break;
        case actionTypes.PUBLISH_POST:
            const toPublished = _unpublishedposts.find(post => 
                post.id === action.post.id
            );
            toPublished.published_date = new Date().toISOString();
            const reverse = _publishedposts.reverse();
            reverse.push(toPublished);
            _publishedposts = reverse.reverse();
            _unpublishedposts = _unpublishedposts.filter(post => 
                post.id !== parseInt(action.post.id, 10)
            )
            store.emitChange();
            break;
        case actionTypes.DELETE_POST:
            _unpublishedposts = _unpublishedposts.filter(post => 
                post.id !== parseInt(action.id, 10)
            )
            store.emitChange();
            break;
        case actionTypes.CREATE_COMMENT:
            store.emitChange();
            break;
        case actionTypes.APPROVE_COMMENT:
            store.emitChange();
            break;
        case actionTypes.DELETE_COMMENT:
            store.emitChange();
            break;
        default:
            // Do nothing
    }
});

export default store;
