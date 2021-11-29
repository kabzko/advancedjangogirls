import React from "react";
import PropTypes from "prop-types";

function TextArea(props) {
    let wrapperClase = "form-control";
    if (props.error && props.error.length > 0) {
        wrapperClase += " is-invalid";
    }
    return ( 
        <div>
            <label htmlFor={props.id}>{props.label}</label>
            <textarea className={wrapperClase}
                id={props.id} 
                name={props.name} 
                onChange={props.onChange} 
                value={props.value} 
            />
            <div className="invalid-feedback">
                {props.error}
            </div>
        </div>
    )
}

TextArea.propTypes = {
    id: PropTypes.string.isRequired,
    name: PropTypes.string.isRequired,
    label: PropTypes.string.isRequired,
    onChange: PropTypes.func.isRequired,
    value: PropTypes.string,
    error: PropTypes.string,
}

TextArea.defaultProps = {
    error: ""
}

export default TextArea;