"use client";

import React, { useState } from "react";
import styles from "./register.module.css"
import LoginForm from "@/components/loginForm/loginForm";
import RegisterForm from "@/components/registerForm/registerForm";

const LoginRegisterPage = () => {
    const [currentForm, setCurrentForm] = useState("register");

    const toggleForm = (formName) => {
        setCurrentForm(formName);
    };

    return (
        <div className={styles.container}>
            {currentForm === "register" ? (
                <RegisterForm onFormSwitch={toggleForm} />
            ) : (
                    <LoginForm onFormSwitch={toggleForm} />
            )}
        </div>
    );
};

export default LoginRegisterPage;
