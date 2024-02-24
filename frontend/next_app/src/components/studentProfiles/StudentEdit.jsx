import React, { useState, useEffect } from 'react';
import './StudentEdit.module.css';

const StudentEdit = ({ userProfile, onUpdate, onToggleEditMode }) => {
    const [editMode, setEditMode] = useState(false);
    const [formData, setFormData] = useState(userProfile);

    useEffect(() => {
        setFormData(userProfile); // update local when props update
    }, [userProfile]);

    const handleInputChange = (e, field, index = null, subField = null) => {
        const newArray = [...formData[field]];
        if (subField !== null) {
            newArray[index][subField] = e.target.value;
        } else {
            newArray[index] = e.target.value;
        }
        setFormData({ ...formData, [field]: newArray });
    };


    const handleSubmit = (e) => {
        e.preventDefault();
        onUpdate(formData);
        setEditMode(false);
        onToggleEditMode();
    };

    const handleEditClick = () => {
        setEditMode(true);
        onToggleEditMode();
    };

    const handleCancel = () => {
        setEditMode(false);
        onToggleEditMode();
    };



    if (editMode) {
        return (
            <form onSubmit={handleSubmit}>
                {/* Sample Items */}
                <div className="form-group">
                    <label>
                        Name:
                        <input type="text" value={formData.name} onChange={(e) => handleInputChange(e, 'name')}/>
                    </label>
                </div>

                <div className="form-group">
                    <label>
                        Teaching Subjects:
                        <input type="text" defaultValue={userProfile.subject}/>
                    </label>
                </div>
                <div className="form-group">
                    <label>
                        One line introduce:
                        <input type="text" defaultValue={userProfile.tagline}/>
                    </label>
                </div>


                <div className="form-actions">
                    <button type="submit">Save</button>
                    <button onClick={handleCancel}>Cancel</button>
                </div>
            </form>
        );
    }

    return (
        <div>
            <button onClick={handleEditClick}>Edit</button>
        </div>
    );
};

export default StudentEdit;
