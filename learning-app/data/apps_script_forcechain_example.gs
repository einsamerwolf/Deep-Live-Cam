/**
 * Minimales Beispiel für Force-Ketten-Logik (Google Apps Script).
 */
function answer(questionId, selectedOption) {
  const q = getQuestionById(questionId); // aus CSV/Sheet
  const isCorrect = selectedOption === q.correct_option;

  if (isCorrect) {
    return {
      ok: true,
      next_question_id: null,
      move_normal_flow: true,
      explanation: q.explanation
    };
  }

  return {
    ok: false,
    next_question_id: q.alt_question_id || null,
    move_normal_flow: !q.alt_question_id,
    explanation: q.explanation
  };
}

function loadQuestion(forceId) {
  if (forceId) {
    return getQuestionById(forceId);
  }
  return getNextQuestionInNormalOrder();
}
