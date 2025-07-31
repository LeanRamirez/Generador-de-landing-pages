import React, { useRef, useEffect } from "react";
import styles from "../styles/components/LandingPreview.module.css";

const LandingPreview = ({ htmlContent, isVisible = true }) => {
  const iframeRef = useRef(null);

  useEffect(() => {
    if (iframeRef.current && htmlContent) {
      const iframe = iframeRef.current;
      const iframeDoc = iframe.contentDocument || iframe.contentWindow.document;

      // Escribir el contenido HTML en el iframe
      iframeDoc.open();
      iframeDoc.write(htmlContent);
      iframeDoc.close();
    }
  }, [htmlContent]);

  if (!isVisible || !htmlContent) {
    return null;
  }

  return (
    <div className={styles.previewContainer}>
      <div className={styles.previewHeader}>
        <h3>Vista Previa de la Landing Page</h3>
        <div className={styles.deviceButtons}>
          <button
            className={`${styles.deviceButton} ${styles.desktop}`}
            onClick={() => {
              const iframe = iframeRef.current;
              if (iframe) {
                iframe.style.width = "100%";
                iframe.style.height = "600px";
              }
            }}
            title="Vista Desktop"
          >
            🖥️
          </button>
          <button
            className={`${styles.deviceButton} ${styles.tablet}`}
            onClick={() => {
              const iframe = iframeRef.current;
              if (iframe) {
                iframe.style.width = "768px";
                iframe.style.height = "600px";
              }
            }}
            title="Vista Tablet"
          >
            📱
          </button>
          <button
            className={`${styles.deviceButton} ${styles.mobile}`}
            onClick={() => {
              const iframe = iframeRef.current;
              if (iframe) {
                iframe.style.width = "375px";
                iframe.style.height = "600px";
              }
            }}
            title="Vista Mobile"
          >
            📱
          </button>
        </div>
      </div>

      <div className={styles.iframeWrapper}>
        <iframe
          ref={iframeRef}
          className={styles.previewIframe}
          title="Landing Page Preview"
          sandbox="allow-same-origin allow-scripts"
          frameBorder="0"
        />
      </div>

      <div className={styles.previewFooter}>
        <p className={styles.previewNote}>
          Esta es una vista previa de tu landing page. El diseño es
          completamente responsivo.
        </p>
      </div>
    </div>
  );
};

export default LandingPreview;
