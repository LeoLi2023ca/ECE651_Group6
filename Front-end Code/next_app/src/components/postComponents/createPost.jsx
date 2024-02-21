import React, { useState } from 'react';
import CreateInfoBox from './createInfoBox';

const CreatePost = ({ student_id, student_name }) => {
    // Initialize form data state
    const [newPost, setNewPost] = useState({
        postID: '', // will be generated at commit time
        student_id,
        student_name,
        subject_name: '',
        date: '',
        msg: '',
        salary: '',
        available_time: '',
        status: '',
        title: '',
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setNewPost({
            ...newPost,
            [name]: value,
        });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        // Auto-generated postID
        const postID = `100`;
        const updatedFormData = { ...newPost, postID };

        // Send updatedFormData to the server here...
    };

    return (
        <div>
            <CreateInfoBox post={newPost} handleChange={handleChange} />
            <button onClick={handleSubmit}>Submit</button>
        </div>
    );
};

export default CreatePost;
