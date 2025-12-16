// comments.js
document.addEventListener("DOMContentLoaded", () => {
  const commentForm = document.getElementById("commentForm");
  const commentText = document.getElementById("id_body");

  // --------------------------
  // Handle Edit Buttons
  // --------------------------
  document.querySelectorAll(".btn-edit").forEach(button => {
    button.addEventListener("click", e => {
      const commentId = e.target.getAttribute("comment_id");
      const commentContent = document.getElementById(`comment${commentId}`).innerText;

      // Populate form with comment text
      commentText.value = commentContent;

      // Update form action URL
      commentForm.setAttribute("action", `edit_comment/${commentId}`);

      // Focus textarea for editing
      commentText.focus();
    });
  });

  // --------------------------
  // Handle Delete Buttons
  // --------------------------
  // Optional: Using a modal for confirmation
  document.querySelectorAll(".btn-delete").forEach(button => {
    button.addEventListener("click", e => {
      const commentId = e.target.getAttribute("comment_id");
      const deleteConfirm = document.getElementById("deleteConfirm"); // modal confirm button
      deleteConfirm.href = `delete_comment/${commentId}`;

      // Open Bootstrap modal
      const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
      deleteModal.show();
    });
  });
});