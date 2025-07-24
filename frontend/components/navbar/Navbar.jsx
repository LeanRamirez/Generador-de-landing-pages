import styles from "../../styles/Navbar.module.css";

export const NavBar = () => {
  return (
    <nav className={styles.container}>
      <div className={styles.logo}>Logo</div>
      <div className={styles.buttons}>
        <button className={styles.viewButton}>View code</button>
        <button className={styles.publishButton}>Publish</button>
        <button className={styles.saveButton}>Save</button>
      </div>
    </nav>
  );
};
