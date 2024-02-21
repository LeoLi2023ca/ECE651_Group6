import styles from "./studentHistoryPost.module.css"
import PostList from "@/components/postComponents/postList";


const StudentHistoryPostPage = () => {
    return (
        <div className={styles.container}>
            <PostList/>
        </div>
    )

};

export default StudentHistoryPostPage;