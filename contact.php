<?php
/**
 * Contact form mail handler for p3mai.com.
 * Receives the form POST (name, email, phone, message) and emails it to
 * the domain mailbox. Returns JSON consumed by script.js.
 */

header('Content-Type: application/json');

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['ok' => false, 'error' => 'method']);
    exit;
}

$name    = trim($_POST['name'] ?? '');
$email   = trim($_POST['email'] ?? '');
$phone   = trim($_POST['phone'] ?? '');
$message = trim($_POST['message'] ?? '');

/* Honeypot: the "website" field is hidden from humans; anything filling it
   is a bot. Report success so the bot moves on, send nothing. */
if (trim($_POST['website'] ?? '') !== '') {
    echo json_encode(['ok' => true]);
    exit;
}

if ($name === '' || $message === '' || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
    http_response_code(400);
    echo json_encode(['ok' => false, 'error' => 'validation']);
    exit;
}

if (strlen($name) > 200 || strlen($email) > 200 || strlen($phone) > 60 || strlen($message) > 20000) {
    http_response_code(400);
    echo json_encode(['ok' => false, 'error' => 'too_long']);
    exit;
}

/* Strip CR/LF from anything that reaches a mail header (header-injection guard). */
$name  = str_replace(["\r", "\n"], ' ', $name);
$email = str_replace(["\r", "\n"], '', $email);
$phone = str_replace(["\r", "\n"], ' ', $phone);

$to      = 'drcolvin@p3mai.com';
$subject = 'P3MAI website enquiry from ' . $name;

$body = "Name:  $name\n"
      . "Email: $email\n"
      . ($phone !== '' ? "Phone: $phone\n" : '')
      . "\nMessage:\n$message\n"
      . "\n--\nSent from the p3mai.com contact form on " . date('Y-m-d H:i:s T');

/* From must be a domain address for SPF/DMARC to pass on shared hosting;
   Reply-To carries the visitor so replying in the mail client just works. */
$headers = implode("\r\n", [
    'From: P3MAI Website <noreply@p3mai.com>',
    'Reply-To: ' . $name . ' <' . $email . '>',
    'Content-Type: text/plain; charset=UTF-8',
]);

$sent = mail($to, $subject, $body, $headers);

if (!$sent) {
    http_response_code(500);
}
echo json_encode(['ok' => (bool) $sent]);
