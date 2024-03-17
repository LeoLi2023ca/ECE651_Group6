<template>
    <a-layout style="padding: 0px 30px 0px">
        <a-layout-content
            :style="{ background: '#fff', padding: '80px', minHeight: '80vh', display: 'flex', justifyContent: 'center', alignItems: 'center' }">

            <a-form ref="formRef" name="custom-validation" :model="formState" :rules="rules" v-bind="layout"
                @finish="handleFinish" @validate="handleValidate" @finishFailed="handleFinishFailed"
                :label-col="labelCol" :wrapper-col="wrapperCol">
                <a-typography-title :level="4">Update Password</a-typography-title>
                <a-form-item has-feedback label="Old" name="old_pass">
                    <a-input v-model:value="formState.oldPass" type="password" autocomplete="off" />
                </a-form-item>
                <a-form-item has-feedback label="New" name="pass">
                    <a-input v-model:value="formState.pass" type="password" autocomplete="off" />
                </a-form-item>
                <a-form-item has-feedback label="Confirm" name="checkPass">
                    <a-input v-model:value="formState.checkPass" type="password" autocomplete="off" />
                </a-form-item>
                <a-form-item :wrapper-col="{ span: 14, offset: 4 }">
                    <a-button type="primary" html-type="submit">Submit</a-button>
                </a-form-item>
            </a-form>
        </a-layout-content>
    </a-layout>
</template>
<script setup>
import { reactive, ref } from 'vue';
import axios from 'axios';
import { message } from 'ant-design-vue';

const formRef = ref();
const formState = reactive({
    oldPass: '',
    pass: '',
    checkPass: '',
});
const labelCol = {
    style: {
        width: '80px',
    },
};
const wrapperCol = {
    span: 20,
};

const validatePass = async (_rule, value) => {
    if (value === '') {
        return Promise.reject('Please input the new password');
    } else {
        if (formState.checkPass !== '') {
            formRef.value.validateFields('checkPass');
        }
        return Promise.resolve();
    }
};
const validatePass2 = async (_rule, value) => {
    if (value === '') {
        return Promise.reject('Please input the new password again');
    } else if (value !== formState.pass) {
        return Promise.reject("Two inputs don't match!");
    } else {
        return Promise.resolve();
    }
};
const rules = {
    oldPass: [
        {
            required: true,
            validator: validatePass,
            trigger: 'change',
        }
    ],
    pass: [
        {
            required: true,
            validator: validatePass,
            trigger: 'change',
        },
    ],
    checkPass: [
        {
            required: true,
            validator: validatePass2,
            trigger: 'change',
        },
    ],
};
const layout = {
    labelCol: {
        span: 24,
    },
    wrapperCol: {
        span: 14,
    },
};

function updatePassword() {
    var data = new FormData();
    const user_info = JSON.parse(sessionStorage.getItem('user_info'))
    data.append('username', user_info.username)
    data.append('old_pass', formState.oldPass)
    data.append('new_pass', formState.pass)

    var config = {
        method: 'post',
        url: 'http://localhost:5000/updatePassword',
        data: data
    };

    axios(config)
        .then(function (response) {
            console.log(response);
            formState.oldPass = '';
            formState.checkPass = '';
            formState.pass = '';
            message.success('Password updated successfully!');
        })
        .catch(function (error) {
            console.log(error);
            formState.oldPass = '';
            formState.checkPass = '';
            formState.pass = '';
            message.error('Old password incorrect!');
        });
}

const handleFinish = values => {
    updatePassword();
    console.log(values, formState);
};
const handleFinishFailed = errors => {
    console.log(errors);

};
const handleValidate = (...args) => {
    console.log(args);
};
</script>