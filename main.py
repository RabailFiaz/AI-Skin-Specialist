#logic + UI
from pathlib import Path

import gradio as gr

#from brain_of_the_doctor import brain_of_the_doctor
from doctors_brain import brain_of_the_doctor
from doctors_voice import convert_text_to_doctor_audio
from voice_of_patient import transcribe_patient_voice


APP_TITLE = "AI Skin Specialist"

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..700;1,9..144,400..600&family=Inter:wght@400..700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap');

:root {
    --ais-bg: #f1f4ec;
    --ais-surface: #ffffff;
    --ais-surface-warm: #fbf8f2;
    --ais-surface-low: #eef1e7;
    --ais-border: #dee4d5;
    --ais-border-strong: #b6c0a9;
    --ais-ink: #1b241f;
    --ais-muted: #5c6759;
    --ais-clay: #c1502e;
    --ais-clay-dark: #9c3c20;
    --ais-clay-soft: #f4ddcd;
    --ais-gold: #c1932f;
    --ais-radius-hero: 26px;
    --ais-radius-lg: 18px;
    --ais-radius-md: 12px;
    --ais-shadow: 0 20px 44px rgba(27, 36, 31, 0.09);
    --body-background-fill: #f1f4ec;
    --body-text-color: #1b241f;
    --background-fill-primary: #ffffff;
    --background-fill-secondary: #eef1e7;
    --block-background-fill: #ffffff;
    --block-border-color: #dee4d5;
    --block-info-text-color: #5c6759;
    --block-label-background-fill: #ffffff;
    --block-label-border-color: #dee4d5;
    --block-label-text-color: #5c6759;
    --input-background-fill: #ffffff;
    --input-background-fill-focus: #ffffff;
    --input-border-color: #dee4d5;
    --input-border-color-focus: #c1502e;
    --input-placeholder-color: #97a189;
    --button-primary-background-fill: #c1502e;
    --button-primary-background-fill-hover: #9c3c20;
    --button-primary-text-color: #fffaf5;
    color-scheme: light;
}

* {
    box-sizing: border-box;
}

.gradio-container {
    background:
        radial-gradient(circle at 8% -10%, rgba(193, 80, 46, 0.08) 0%, transparent 45%),
        radial-gradient(circle at 100% 0%, rgba(193, 147, 47, 0.08) 0%, transparent 40%),
        var(--ais-bg) !important;
    color: var(--ais-ink) !important;
    font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif !important;
}

.gradio-container,
.gradio-container * {
    color-scheme: light !important;
}

.ais-shell {
    max-width: 1220px;
    margin: 0 auto;
    padding: 36px 32px 52px;
}

.ais-topbar {
    align-items: center;
    background: var(--ais-surface-warm);
    border: 1px solid var(--ais-border);
    border-radius: var(--ais-radius-hero);
    display: flex;
    justify-content: space-between;
    margin-bottom: 30px;
    padding: 24px 30px;
    position: relative;
    overflow: hidden;
}

.ais-topbar::after {
    content: "";
    position: absolute;
    right: -60px;
    top: -60px;
    width: 200px;
    height: 200px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(193, 80, 46, 0.14), transparent 70%);
}

.ais-brand {
    align-items: center;
    display: flex;
    gap: 16px;
    position: relative;
    z-index: 1;
}

.ais-brand-mark {
    align-items: center;
    background: var(--ais-clay);
    border-radius: 14px;
    color: #fffaf5;
    display: inline-flex;
    font-family: 'Material Symbols Outlined';
    font-size: 24px;
    height: 48px;
    justify-content: center;
    width: 48px;
    flex-shrink: 0;
    transform: rotate(-4deg);
}

.ais-brand h1 {
    color: var(--ais-ink);
    font-family: Fraunces, serif;
    font-size: 27px;
    font-style: italic;
    font-weight: 550;
    letter-spacing: -0.01em;
    line-height: 32px;
    margin: 0;
}

.ais-brand p {
    color: var(--ais-muted);
    font-size: 13px;
    font-weight: 500;
    line-height: 18px;
    margin: 3px 0 0;
}

.ais-security {
    align-items: center;
    background: var(--ais-surface);
    border: 1px solid var(--ais-border);
    border-radius: 999px;
    color: var(--ais-clay-dark);
    display: flex;
    font-size: 12.5px;
    font-weight: 600;
    gap: 8px;
    padding: 9px 16px;
    position: relative;
    z-index: 1;
}

.ais-security .ais-icon {
    color: var(--ais-clay);
}

.ais-icon {
    font-family: 'Material Symbols Outlined';
    font-size: 20px;
    font-variation-settings: 'FILL' 0, 'wght' 450, 'GRAD' 0, 'opsz' 24;
    line-height: 1;
}

.ais-grid {
    align-items: start;
    display: grid;
    gap: 24px;
    grid-template-columns: minmax(0, 5fr) minmax(0, 7fr);
}

.ais-section-title {
    align-items: baseline;
    display: flex;
    gap: 12px;
    margin: 0 0 16px;
}

.ais-section-title .ais-rule {
    background: var(--ais-clay);
    border-radius: 2px;
    height: 20px;
    width: 4px;
}

.ais-section-title h2 {
    color: var(--ais-ink);
    font-family: Fraunces, serif;
    font-size: 21px;
    font-weight: 550;
    line-height: 26px;
    margin: 0;
}

.ais-card {
    background: var(--ais-surface);
    border: 1px solid var(--ais-border);
    border-radius: var(--ais-radius-lg);
    box-shadow: var(--ais-shadow);
    padding: 22px;
}

.ais-input-card {
    display: flex;
    flex-direction: column;
    gap: 18px;
}

.ais-field-label {
    color: var(--ais-ink);
    display: block;
    font-size: 14px;
    font-weight: 600;
    margin-bottom: 4px;
}

.ais-media-row {
    display: grid;
    gap: 14px;
    grid-template-columns: repeat(2, minmax(0, 1fr));
}

.ais-submit-wrap .gr-button-primary {
    background: var(--ais-clay) !important;
    border: 0 !important;
    border-radius: var(--ais-radius-md) !important;
    box-shadow: 0 12px 24px rgba(193, 80, 46, 0.30) !important;
    color: #fffaf5 !important;
    font-size: 16px !important;
    font-weight: 650 !important;
    min-height: 56px !important;
    transition: background 0.15s ease, transform 0.15s ease !important;
}

.ais-submit-wrap .gr-button-primary:hover {
    background: var(--ais-clay-dark) !important;
    transform: translateY(-1px);
}

.ais-note {
    align-items: flex-start;
    background: var(--ais-clay-soft);
    border-radius: var(--ais-radius-md);
    color: #6b2f16;
    display: flex;
    gap: 10px;
    padding: 13px 15px;
}

.ais-note span:not(.ais-icon) {
    color: #6b2f16 !important;
    font-size: 13px;
    font-weight: 500;
    line-height: 18px;
}

.ais-note .ais-icon {
    color: var(--ais-clay-dark) !important;
    flex-shrink: 0;
}

.ais-response-card {
    background: var(--ais-surface-warm);
    border-radius: var(--ais-radius-hero);
    min-height: 560px;
}

.ais-empty {
    align-items: center;
    color: var(--ais-muted);
    display: flex;
    flex-direction: column;
    gap: 14px;
    justify-content: center;
    min-height: 160px;
    text-align: center;
}

.ais-empty .ais-icon {
    align-items: center;
    background: var(--ais-clay-soft);
    border-radius: 999px;
    color: var(--ais-clay-dark);
    display: inline-flex;
    font-size: 36px;
    height: 80px;
    justify-content: center;
    width: 80px;
}

.ais-empty strong {
    color: var(--ais-ink) !important;
    display: block;
    font-family: Fraunces, serif;
    font-size: 19px;
    font-weight: 550;
    line-height: 25px;
    margin-bottom: 4px;
}

.ais-panel-copy {
    color: var(--ais-muted);
    font-size: 13px;
    font-weight: 450;
    line-height: 19px;
    margin: 0;
    max-width: 360px;
}

.ais-output-stack {
    display: flex;
    flex-direction: column;
    gap: 16px;
}

.ais-output-stack .gradio-textbox textarea {
    background: var(--ais-surface) !important;
    border: 0 !important;
    color: var(--ais-ink) !important;
    font-size: 15.5px !important;
    line-height: 23px !important;
}

.ais-transcript textarea {
    color: var(--ais-muted) !important;
    font-style: italic;
}

.ais-audio {
    border-top: 1px solid var(--ais-border);
    padding-top: 16px;
}

.ais-footer {
    align-items: center;
    background: transparent;
    color: var(--ais-muted);
    display: flex;
    font-size: 12.5px;
    justify-content: space-between;
    margin-top: 30px;
    padding: 4px 6px;
}

.ais-footer strong {
    color: var(--ais-ink);
    font-family: Fraunces, serif;
    font-weight: 550;
}

.ais-footer-links {
    display: flex;
    gap: 18px;
}

.ais-card .wrap,
.ais-card .block,
.ais-card .form,
.ais-card .gradio-container,
.ais-card .gradio-row {
    background: transparent !important;
    border: 0 !important;
    box-shadow: none !important;
}

.ais-card .gradio-audio,
.ais-card .gradio-image,
.ais-card .gradio-video,
.ais-card .gradio-textbox {
    background: transparent !important;
    border: 0 !important;
    color: var(--ais-ink) !important;
}

.ais-card .gradio-audio > div,
.ais-card .gradio-image > div,
.ais-card .gradio-video > div,
.ais-card .gradio-textbox > div {
    background: var(--ais-surface-low) !important;
    border: 1px solid var(--ais-border) !important;
    border-radius: var(--ais-radius-md) !important;
    color: var(--ais-ink) !important;
}

.ais-response-card .gradio-textbox > div {
    background: var(--ais-surface) !important;
}

.ais-card .gradio-audio [class*="container"],
.ais-card .gradio-image [class*="container"],
.ais-card .gradio-video [class*="container"],
.ais-card .gradio-textbox [class*="container"],
.ais-card .gradio-audio [class*="wrap"],
.ais-card .gradio-image [class*="wrap"],
.ais-card .gradio-video [class*="wrap"],
.ais-card .gradio-textbox [class*="wrap"] {
    background: var(--ais-surface-low) !important;
    border-color: var(--ais-border) !important;
    color: var(--ais-ink) !important;
}

.ais-response-card .gradio-textbox [class*="container"],
.ais-response-card .gradio-textbox [class*="wrap"] {
    background: var(--ais-surface) !important;
}

.ais-card .gradio-audio button,
.ais-card .gradio-image button,
.ais-card .gradio-video button,
.ais-card .gradio-textbox button {
    color: var(--ais-clay-dark) !important;
}

.ais-card [data-testid="block-label"],
.ais-card div[class*="block-label"],
.ais-card label[class*="container"] {
    background: transparent !important;
    border: 0 !important;
    color: var(--ais-muted) !important;
}

.ais-card [data-testid="block-label"] *,
.ais-card div[class*="block-label"] *,
.ais-card label[class*="container"] * {
    color: var(--ais-muted) !important;
}

.ais-card label span,
.ais-output-stack label span {
    color: var(--ais-muted) !important;
    font-size: 13px !important;
    font-weight: 600 !important;
}

.ais-card input,
.ais-card textarea,
.ais-card select,
.ais-card .upload-container,
.ais-card .file-preview,
.ais-card .input-container,
.ais-card .dropzone,
.ais-card .empty,
.ais-card .icon-wrap,
.ais-card video,
.ais-card img {
    background: var(--ais-surface-low) !important;
    border-color: var(--ais-border) !important;
    color: var(--ais-ink) !important;
    border-radius: var(--ais-radius-md) !important;
}

.ais-card input:disabled,
.ais-card textarea:disabled,
.ais-card [aria-disabled="true"],
.ais-card .disabled {
    background: var(--ais-surface-low) !important;
    color: var(--ais-ink) !important;
    opacity: 1 !important;
    -webkit-text-fill-color: var(--ais-ink) !important;
}

.ais-card .upload-container,
.ais-card .dropzone {
    min-height: 200px !important;
    transition: border-color 0.15s ease, background 0.15s ease;
}

.ais-card .dropzone:hover {
    background: var(--ais-clay-soft) !important;
    border-color: var(--ais-clay) !important;
}

.ais-card .gradio-audio .upload-container,
.ais-card .gradio-audio .dropzone {
    min-height: 110px !important;
}

.ais-media-row .gradio-image,
.ais-media-row .gradio-video,
.ais-media-row .gradio-image > div,
.ais-media-row .gradio-video > div,
.ais-media-row .gradio-image [class*="container"],
.ais-media-row .gradio-video [class*="container"],
.ais-media-row .gradio-image [class*="wrap"],
.ais-media-row .gradio-video [class*="wrap"] {
    min-height: 260px !important;
    overflow: visible !important;
}

.ais-media-row .gradio-image .upload-container,
.ais-media-row .gradio-video .upload-container,
.ais-media-row .gradio-image .dropzone,
.ais-media-row .gradio-video .dropzone {
    height: 200px !important;
    min-height: 200px !important;
}

.ais-media-row .gradio-image button,
.ais-media-row .gradio-video button {
    min-height: 34px !important;
}

.ais-card .upload-container *,
.ais-card .file-preview *,
.ais-card .input-container *,
.ais-card .dropzone *,
.ais-card .empty * {
    color: var(--ais-ink) !important;
}

.ais-card ::placeholder {
    color: var(--ais-border-strong) !important;
}

@media (max-width: 900px) {
    .ais-shell {
        padding: 22px;
    }

    .ais-topbar,
    .ais-footer {
        align-items: flex-start;
        flex-direction: column;
        gap: 14px;
    }

    .ais-grid,
    .ais-media-row {
        grid-template-columns: 1fr;
    }

    .ais-section-title h2 {
        font-size: 19px;
        line-height: 25px;
    }
}
"""


def process_inputs(audio_filepath, image_filepath, video_filepath):
    if not audio_filepath:
        raise gr.Error("Please record or upload your voice description first.")

    if not image_filepath and not video_filepath:
        raise gr.Error("Please upload a skin image or video before analysis.")

    patient_text = transcribe_patient_voice(audio_filepath)
    doctor_text = brain_of_the_doctor(
        patient_text=patient_text,
        image_filepath=image_filepath,
        video_filepath=video_filepath,
    )
    doctor_audio = convert_text_to_doctor_audio(doctor_text)

    return patient_text, doctor_text, str(Path(doctor_audio))


with gr.Blocks(title=APP_TITLE) as iface:
    with gr.Column(elem_classes="ais-shell"):
        gr.HTML(
            """
            <header class="ais-topbar">
                <div class="ais-brand">
                    <span class="ais-brand-mark ais-icon">spa</span>
                    <div>
                        <h1>AI Skin Specialist</h1>
                        <p>Voice, image and video based skin consultation</p>
                    </div>
                </div>
                <div class="ais-security">
                    <span class="ais-icon">verified_user</span>
                    <span>Privacy-first consultation</span>
                </div>
            </header>
            """
        )

        with gr.Row(elem_classes="ais-grid"):
            with gr.Column(scale=5):
                gr.HTML(
                    """
                    <div class="ais-section-title">
                        <span class="ais-rule"></span>
                        <h2>Patient input</h2>
                    </div>
                    """
                )

                with gr.Column(elem_classes="ais-card ais-input-card"):
                    gr.HTML('<span class="ais-field-label">Describe your skin concern</span>')
                    audio_input = gr.Audio(
                        sources=["microphone", "upload"],
                        type="filepath",
                        label="Patient voice",
                    )

                    with gr.Row(elem_classes="ais-media-row"):
                        image_input = gr.Image(
                            type="filepath",
                            label="Skin image",
                            height=280,
                        )
                        video_input = gr.Video(label="Skin video", height=280)

                    with gr.Column(elem_classes="ais-submit-wrap"):
                        analyze_button = gr.Button(
                            "Analyze concern",
                            variant="primary",
                            size="lg",
                        )

                    gr.HTML(
                        """
                        <div class="ais-note">
                            <span class="ais-icon">info</span>
                            <span>For a better assessment, include a short video showing the affected area from multiple angles and under good lighting.</span>
                        </div>
                        """
                    )

            with gr.Column(scale=7):
                gr.HTML(
                    """
                    <div class="ais-section-title">
                        <span class="ais-rule"></span>
                        <h2>Doctor response</h2>
                    </div>
                    """
                )

                with gr.Column(elem_classes="ais-card ais-response-card"):
                    gr.HTML(
                        """
                        <div class="ais-empty">
                            <span class="ais-icon">pending_actions</span>
                            <div>
                                <strong>Ready for analysis</strong>
                                <p class="ais-panel-copy">Your consultation summary, transcript, and guidance will appear below after analysis.</p>
                            </div>
                        </div>
                        """
                    )

                    with gr.Column(elem_classes="ais-output-stack"):
                        transcript_output = gr.Textbox(
                            label="Your speech transcript",
                            lines=4,
                            interactive=False,
                            elem_classes="ais-transcript",
                        )
                        response_output = gr.Textbox(
                            label="Doctor's guidance",
                            lines=9,
                            interactive=False,
                        )
                        audio_output = gr.Audio(
                            label="Doctor voice response",
                            type="filepath",
                            autoplay=True,
                            elem_classes="ais-audio",
                        )

                gr.HTML(
                    """
                    <div class="ais-security" style="justify-content:center; margin-top:16px; background:transparent; border:0; padding:0;">
                        <span class="ais-icon">verified</span>
                        <span style="color:var(--ais-muted); font-weight:500;">AI guidance is informational and not a medical diagnosis</span>
                    </div>
                    """
                )

        gr.HTML(
            """
            <footer class="ais-footer">
                <div><strong>AI Skin Specialist</strong> — consult a licensed dermatologist for urgent or serious symptoms.</div>
                <div class="ais-footer-links">
                    <span>Privacy policy</span>
                    <span>Terms of service</span>
                    <span>Medical disclaimer</span>
                </div>
            </footer>
            """
        )

    analyze_button.click(
        fn=process_inputs,
        inputs=[audio_input, image_input, video_input],
        outputs=[transcript_output, response_output, audio_output],
    )


if __name__ == "__main__":
    iface.launch(debug=True, css=CSS, theme=gr.themes.Base())