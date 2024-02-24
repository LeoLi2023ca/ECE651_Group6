import React, { useState, useEffect } from 'react';
import './EditProfile.module.css';

const EditProfile = ({ userProfile, onUpdate, onToggleEditMode }) => {
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

    const handleAddItem = (field, newItem) => {
        setFormData({ ...formData, [field]: [...formData[field], newItem] });
    };

    const handleDeleteItem = (field, index) => {
        const newArray = [...formData[field]];
        newArray.splice(index, 1);
        setFormData({ ...formData, [field]: newArray });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        onUpdate(formData); // Calling the update logic
        setEditMode(false); // Exit Edit mode
        onToggleEditMode(); // Notify the parent component that the editing mode has changed
    };

    const handleEditClick = () => {
        setEditMode(true); // Enter Edit mode
        onToggleEditMode(); // Notify the parent component that the editing mode has changed
    };

    const handleCancel = () => {
        setEditMode(false); // Exit Edit mode
        onToggleEditMode(); // Notify the parent component that the editing mode has changed
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
                <div className="form-group">
                    <label>
                        Highest Degree:
                        <input type="text" defaultValue={userProfile.highestDegree}/>
                    </label>
                </div>
                <div className="form-group">
                    <label>
                        Graduated School:
                        <input type="text" defaultValue={userProfile.graduatedFrom}/>
                    </label>
                </div>
                <div className="form-group">
                    <label>
                        Year of Birth:
                        <input type="text" defaultValue={userProfile.birthYear}/>
                    </label>
                </div>
                <div className="form-group">
                    <label>
                        Certifications:
                        <input type="text" defaultValue={userProfile.certifications}/>
                    </label>
                </div>


                {/* Package */}
                <div className="form-group">
                    {formData.package.map((pkg, index) => (
                        <div key={index} className="array-item">
                            <label>Duration: <input type="number" value={pkg.duration}
                                                    onChange={(e) => handleInputChange(e, 'package', index, 'duration')}/></label>
                            <label>Price: <input type="text" value={pkg.price}
                                                 onChange={(e) => handleInputChange(e, 'package', index, 'price')}/></label>
                            <label>Sessions: <input type="number" value={pkg.sessions}
                                                    onChange={(e) => handleInputChange(e, 'package', index, 'sessions')}/></label>
                            <label>Discount: <input type="text" value={pkg.discount || ''}
                                                    onChange={(e) => handleInputChange(e, 'package', index, 'discount')}/></label>
                            <button type="button" onClick={() => handleDeleteItem('package', index)}>Delete Package
                                Item
                            </button>
                        </div>
                    ))}
                    <button type="button" onClick={() => handleAddItem('package', {
                        duration: 0,
                        price: '',
                        sessions: 0,
                        discount: ''
                    })}>Add Package Item
                    </button>
                </div>
                {/* faqs */}
                <div className="form-group">
                    {formData.faqs.map((faq, index) => (
                        <div key={index} className="array-item">
                            <label>Question: <input type="text" value={faq.question}
                                                    onChange={(e) => handleInputChange(e, 'faqs', index, 'question')}/></label>
                            <label>Answer: <input type="text" value={faq.answer}
                                                  onChange={(e) => handleInputChange(e, 'faqs', index, 'answer')}/></label>
                            <button type="button" onClick={() => handleDeleteItem('faqs', index)}>Delete FAQ</button>
                        </div>
                    ))}
                    <button type="button" onClick={() => handleAddItem('faqs', {question: '', answer: ''})}>Add FAQ
                    </button>
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

export default EditProfile;
